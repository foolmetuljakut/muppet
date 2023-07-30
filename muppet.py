from Parser import Parser

class PackageManager:
    def parsearglist(this):
        parser = Parser()

        parser.addargument("install", "i", "")
        parser.addargument("remove", "r", "")

        parser.addargument("show", "S", "")
        parser.addargument("search", "s", "")

        parser.addargument("download", "d", "")
        parser.addargument("upload", "u", "")
        
        parser.parse()

        if "result" in parser.arguments[0]:
            this.installlist = parser.arguments[0]["result"].split()
        
        if "result" in parser.arguments[1]:
            this.removelist = parser.arguments[1]["result"].split()
        
        if "result" in parser.arguments[2]:
            this.showlist = parser.arguments[2]["result"].split()
        
        if "result" in parser.arguments[3]:
            this.searchlist = parser.arguments[3]["result"].split()
        
        if "result" in parser.arguments[4]:
            this.downloadlist = parser.arguments[4]["result"].split()
        
        if "result" in parser.arguments[5]:
            this.uploadlist = parser.arguments[5]["result"].split()
        
    def run(this):
        this.parsearglist()

        if this.removelist:
            pass
        if this.installlist:
            pass
        if this.showlist:
            pass
        if this.searchlist:
            pass
        if this.downloadlist:
            pass
        if this.uploadlist:
            pass

if __name__ == "__main__":
    
    PackageManager().run()

    print()