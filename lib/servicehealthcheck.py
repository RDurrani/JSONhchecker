def checkhealth(jsonfile):
    #Return status of Jsonfile
    #Will return broken in case of broken JSON file

    def checkservicehealth(jsonfile, servicename):
        #return the health status for a service object within a json file
        #Will return "Invalid" if servicename does not contain healthStatus
        #Will return "Broken" for broken json object

        for check in jsonfile[servicename]:
            if check=="healthStatus":
                if jsonfile[servicename]["healthStatus"]=="Failed":
                    if jsonfile[servicename]["severity"]=="CRITICAL":
                        return "Unhealthy"
                    elif jsonfile[servicename]["severity"]=="NON---CRITICAL":
                        return "Degraded"
                    else:
                        return "Broken" #or call error
                elif jsonfile[servicename]["healthStatus"]=="Passed":
                    return "Healthy"
                else:
                    return "Broken" #or call error
        return "Invalid"



    status = None
    for servicename in jsonfile:
        dat= checkservicehealth(jsonfile, servicename)
        if dat != "Invalid":
            if status != "Broken":
                if dat == "Broken":
                    status = dat
                elif status != "Unhealthy":
                    if dat == "Unhealthy":
                        status = dat
                    elif status != "Degraded":
                        if dat == "Degraded":
                            status = dat
                        elif status != "Healthy":
                            if dat == "Healthy":
                                status = dat
        #print('{service} is {status}. main is {mainstatus}'.format(service=servicename, status=dat, mainstatus=status))
    return status
