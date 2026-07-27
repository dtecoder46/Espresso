lu = require("luaunit")

--[[
-- Name: read_file()
-- Purpose: read the .esp file
-- Parameters: none
-- Return: espresso - the file contents
--]]--

function read_file() 
	espresso_file = io.open("Main.esp", "r")

	espresso = espresso_file:read("*a")

	espresso_file:close()

	return espresso

end



espresso_string = read_file()

os.exit( lu.LuaUnit.run() )
