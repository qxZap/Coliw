import requests





URL = "http://ip-api.com/json/{input}"
#arguments=['ipinfo','208.80.152.201','-lt','-lg','-ct','-c','-r']

def ipinfo(arguments):
    if arguments[0]=="ipinfo":


        if len(arguments)==1:
         r = requests.get('http://ip-api.com/json/').json()
         print(r['country'])
         print(r['regionName'])
         print(r['city'])
        if len(arguments)>=2:
            r = requests.get('http://ip-api.com/json/' + arguments[1]).json()
            options=""
            for i in range(2, len(arguments)):
                options = options+arguments[i]
            options = options.replace("-", "")
            options = options.replace(" ", "")
            flag_c=False
            flag_r=False
            flag_z = False
            flag_ct = False
            flag_lt = False
            flag_lg = False
            print(options)
            for i in range(0, len(options)):
                if options[i] == "c":
                    flag_c = True
                if options[i] == "r":
                    flag_r = True
                if options[i]=="z":
                    flag_z = True
                if "ct" in options:
                    flag_ct = True
                if "lg" in options:
                    flag_lg = True
                if "lt" in options:
                    flag_lt=True

            if flag_c:
                print(r['country'])
            if flag_ct:
                print(r['city'])
            if flag_lt:
                print(r['lat'])
            if flag_lg:
                print(r['lon'])
            if flag_r:
                print(r['regionName'])
            if flag_z:
                print(r['zip'])
