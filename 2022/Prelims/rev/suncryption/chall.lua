local sha = require("sha2")

local key <const> = {71, 73, 66, 70, 76, 65, 71}
local correct <const> = "0ebe2eca800cf7bd9d9d9f9f4aafbc0c77ae155f43bbbeca69cb256a24c7f9bb"


function hash(str) 
    return sha.sha256(str)
end

function is_valid_file(str)
    return correct == hash(str)
end

function read_file(filename)
    file = io.open(filename, "rb")
    if not file then return nil end
    content = file:read "*a"
    file:close()
    return content
end

function decrypt(str)
    arr = {}
    for i = 1, #str do
        arr[i] = str:byte(i) ~ key[((i - 1) % #key) + 1]
    end
    return arr
end

function main()
    io.write("Enter name of encrypted file: ")
    filename = io.read()
    content = read_file(filename)

    if content == nil then
        print("Failed to open " .. filename)
        os.exit(1)
    end

    if not is_valid_file(content) then
        print("INVALID FILE DETECTED!!!")
        print("Expecting " .. correct)
        os.exit(1)
    end

    msg = decrypt(content)
    for _, val in ipairs(msg) do
        io.write(string.char(val))
    end
    io.write("\n")
end

main()
