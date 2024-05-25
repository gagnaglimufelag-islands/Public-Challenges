use rayon::prelude::*;
use sha2::{Digest, Sha256};

#[derive(Clone)]
pub struct Sha2_224 {
    state: [u32; 8],
    block: [u32; 16],
    pub size: usize,
}

impl Sha2_224 {
    pub const IV: [u32; 8] = [
        0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939, 0xffc00b31, 0x68581511, 0x64f98fa7,
        0xbefa4fa4,
    ];
    pub const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
        0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
        0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
        0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
        0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
        0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
        0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
        0xc67178f2,
    ];

    pub fn new() -> Self {
        Self {
            state: Self::IV,
            block: [0; 16],
            size: 0,
        }
    }

    pub fn from(hash: &[u8; 32]) -> Self {
        Self {
            state: [0, 4, 8, 12, 16, 20, 24, 28]
                .map(|i| u32::from_be_bytes([hash[i], hash[i + 1], hash[i + 2], hash[i + 3]])),
            block: [0; 16],
            size: 0,
        }
    }

    pub fn update(&mut self, input_buf: impl AsRef<[u8]>) -> () {
        let mut offset: usize = self.size % 64;
        self.size += input_buf.as_ref().len();

        for &v in input_buf.as_ref() {
            if offset % 4 == 0 {
                self.block[offset >> 2] = (v as u32) << 24;
            } else {
                self.block[offset >> 2] |= (v as u32) << ((3 - (offset & 3)) << 3);
            }
            offset += 1;

            if offset % 64 == 0 {
                self.transform();
                offset = 0;
            }
        }
    }

    fn transform(&mut self) {
        let mut w = [0u32; 80];
        for i in 0..80 {
            if i < 16 {
                w[i] = self.block[i];
            } else {
                let s1 = w[i - 2].rotate_right(17) ^ w[i - 2].rotate_right(19) ^ (w[i - 2] >> 10);
                let s0 = w[i - 15].rotate_right(7) ^ w[i - 15].rotate_right(18) ^ (w[i - 15] >> 3);
                w[i] = s1
                    .wrapping_add(w[i - 7])
                    .wrapping_add(s0)
                    .wrapping_add(w[i - 16]);
            }
        }

        let mut h = self.state;
        for i in 0..64 {
            let s1 = h[4].rotate_right(6) ^ h[4].rotate_right(11) ^ (h[4].rotate_right(25));
            let ch = (h[4] & h[5]) ^ ((!h[4]) & h[6]);

            let v1 = h[7]
                .wrapping_add(s1)
                .wrapping_add(ch)
                .wrapping_add(Self::K[i])
                .wrapping_add(w[i]);

            let s0 = h[0].rotate_right(2) ^ h[0].rotate_right(13) ^ h[0].rotate_right(22);
            let maj = (h[0] & h[1]) ^ (h[0] & h[2]) ^ (h[1] & h[2]);
            let v2 = s0.wrapping_add(maj);

            h[7] = h[6];
            h[6] = h[5];
            h[5] = h[4];
            h[4] = h[3].wrapping_add(v1);
            h[3] = h[2];
            h[2] = h[1];
            h[1] = h[0];
            h[0] = v1.wrapping_add(v2);
        }
        self.state = [0, 1, 2, 3, 4, 5, 6, 7].map(|i| self.state[i].wrapping_add(h[i]));
    }

    pub fn finalize(&mut self) -> [u8; 32] {
        let pad = padding(self.size);
        self.update(&pad);

        let mut digest = [0u8; 32];
        let mut j = 0;
        for i in 0..8 {
            [digest[j], digest[j + 1], digest[j + 2], digest[j + 3]] = self.state[i].to_be_bytes();
            j += 4;
        }

        digest
    }
}

pub fn compute(data: impl AsRef<[u8]>) -> [u8; 28] {
    let mut m = Sha2_224::new();
    m.update(data.as_ref());
    m.finalize()[..28].try_into().unwrap()
}

pub fn padding_len(data_len: usize) -> usize {
    let offset = (data_len % 64) as usize;
    if offset < 56 {
        64 - offset
    } else {
        128 - offset
    }
}

pub fn padding(data_len: usize) -> Vec<u8> {
    let bit_len = data_len.wrapping_mul(8);
    let pad_length: usize = padding_len(data_len);

    let mut pad = vec![0; pad_length];
    pad[0] = 0x80;
    let p: [u8; 8] = bit_len.to_le_bytes();
    for i in 0..8 {
        pad[pad_length - i - 1] = p[i];
    }
    pad
}
fn main() {
    
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: {} <hex value> {} <hex value>", args[0], args[1]);
        std::process::exit(1);
    }
    let s224 = hex::decode(&args[1]).unwrap();
    let s256 = hex::decode(&args[2]).unwrap();

    let orig_size = 17;
    let extended_data = b"admin";
    let v: Vec<u8> = (0..=255).into_iter().collect();
    v.par_iter().map( |&c1| {
        for c2 in 0..=255 {
            for c3 in 0..=255 {
                for c4 in 0..=255 {
                    let mut hash = s224.clone();
                    hash.extend(&[c1,c2,c3,c4]);
                    let mut m = Sha2_224::from(&hash.try_into().unwrap());

                    let pad_length: usize = padding_len(orig_size);
                    m.size = orig_size + pad_length;

                    m.update(extended_data);
                    let mut h = Sha256::new();
                    let token = &m.finalize()[..28];
                    h.update(token);
                    if &h.finalize()[..] == &s256 {
                        println!("{:?}", token);
                        std::process::exit(0x0100)
                    }
                }}}}).collect::<()>();
}
