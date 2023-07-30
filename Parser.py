import sys

class Parser:
    def __init__(this):
        this.options = []
        this.arguments = []

    def decompose(this):
        line = " ".join(sys.argv[1:]) + "-" # "-" serves as a helper and is discarded in the options

        options = []
        ad = False # apostrophe detection
        l = ""
        for i, c in enumerate(line):
            if c == "'":
                ad = not ad
            if not ad:
                if c == "-" and len(l) > 0:
                    options.append(l)
                    l = ""
            l += c

        delctr = 0
        for _i in range(len(options)):
            i = _i - delctr
            if options[i].startswith(" "):
                options[i] = options[i][1:]
            if options[i].endswith(" "):
                options[i] = options[i][:-1]
            if options[i] == "-" and i+1 < len(options):
                options[i] += options[i+1]
                del options[i+1]
                delctr += 1

        this.options = options

    def addargument(this, long : str, short : str, help : str):
        this.arguments.append({
            "long": long,
            "short": short,
            "help": help
        })
    
    def parse(this):
        this.decompose()
        
        for option in this.options:
            while option.startswith("-"):
                option = option[1:]
            firstword = option.split()[0]
            hits = list(filter(lambda a: a["long" if len(firstword) > 1 else "short"] == firstword, this.arguments))

            if len(hits) == 0:
                raise Exception("did not recognize option: \"" + firstword + "\" in " + option)
            
            for hit in hits:
                hit["result"] = option[(len(firstword)+1):]