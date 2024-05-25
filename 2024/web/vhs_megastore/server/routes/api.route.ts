import express from 'express';
import path from 'path';
import fs from 'fs/promises';

const router = express.Router({ mergeParams: true });
router.use(express.json());

interface Owner {
    [key: string]: any;
}

// Function to verify if code matches the owner
const verifyCode = async (ownerName: string, providedCode: string): Promise<boolean> => {
    try {
        const owners = await getOwnerData();
        const owner = owners[ownerName];
        return owner && owner.code === providedCode;
    } catch (error) {
        console.error('Error verifying owner:', error);
        return false;
    }
};

// Function to verify if the owner matches the VHS
const verifyOwner = async (ownerName: string, vhsName: string): Promise<boolean> => {
    try {
        const storage = await getStorageData();
        let selected = null;
        for (const key in storage) {
            if (storage[key].name === vhsName) {
                selected = storage[key];
            }
        }
        if (selected !== null && selected.owner === ownerName) {
            return true;
        }
        return false;
    } catch (error) {
        console.error('Error verifying owner and VHS:', error);
        return false;
    }
};

// Function to get storage data from JSON file
const getStorageData = async (): Promise<{ [key: string]: { owner: string, name: string } }> => {
    const dataPath = path.join(__dirname, '../storage.json');
    const rawData = await fs.readFile(dataPath, 'utf-8');
    return JSON.parse(rawData);
};

// Function to get owner data from JSON file
const getOwnerData = async (): Promise<{ [key: string]: { address: string; code: string } }> => {
    const dataPath = path.join(__dirname, '../owners.json');
    const rawData = await fs.readFile(dataPath, 'utf-8');
    return JSON.parse(rawData);
};

router.post('/retrieve', async (req, res) => {
    try {
        delete req.body["approved"]; // security

        const owners = await getOwnerData();
        const owner: Owner | undefined = owners[req.body.owner_name];

        if (!owner) {
            return res.status(404).send('VHS owner not found');
        }

        const isCodeCorrect = await verifyCode(req.body.owner_name, req.body.code);
        const doesOwnerAndVHSMatch = await verifyOwner(req.body.owner_name, req.body.vhs);

        if (!doesOwnerAndVHSMatch) {
            return res.status(400).send('Invalid owner or VHS');
        }

        const package_info = { ...owner };

        // Get both owner and VHS information
        for (const key in req.body) {
            if (Object.prototype.hasOwnProperty.call(req.body, key)) {
                package_info[key] = req.body[key];
            }
        }

        if (isCodeCorrect) {
            package_info["approved"] = true;
        }

        if (!package_info.approved) {
            return res.status(400).send('Invalid code');
        } else {
            return res.render('retrieve.ejs', { package_info });
        }
    } catch (error) {
        return res.status(500).send('Internal Server Error');
    }
});

export default router;
