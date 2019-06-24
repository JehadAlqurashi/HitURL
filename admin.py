from socket import gethostname,gethostbyname
from urllib import request
from termcolor import colored
print(colored("""

  ###    ##                        
 #   #    #                        
 #        #     ###   # ##   #   # 
 #        #    #   #  ##  #  #   # 
 #  ##    #    #   #  #      #  ## 
 #   #    #    #   #  #       ## # 
  ###    ###    ###   #          # 
                             #   # 
                              ###  Version:0.3
""","cyan"))
print(colored("""
    C0ded By Red Virus
    Designed by Ahlam



""","red"))
print(colored("1: Get Ip Site","yellow"))
print(colored("2: Get Your Ip","yellow"))
print(colored("3: Find admin panel","yellow"))
print(colored("4: Find Shell","yellow"))
x = input(">>> ")
if x == "1":
    print(colored("// Example: google.com","yellow"))
    site = input("Please Enter Your Site: ")
    print("ip",site," is ",gethostbyname(site))
elif x == "2":
    print(gethostbyname(gethostname()))
elif x == "3":
    print(colored("// Example: https://www.google.com","yellow"))
    url =  input("Enter Site >>> ")
    lists = ['admin.php','admin','Login/Admin','admin/login','admin.aspx','admin.asp','administrator','administrator.php','administrator.aspx','administrator.asp','administration','administration.php','administration.aspx','adminLogin','adminlogin.php','adminlogin.aspx','adminlogin.asp','login','login.php','login.aspx','login.asp','adm','manager','manager.php','manager.aspx','manager.asp','access','access.php','access.aspx','access.asp','supervisor','panel.php','panel.aspx','panel.asp','staff','control','control.php','control.aspx','control.asp','member','member.php','member.aspx','member.asp','manage','manage.php','manage.aspx','manage.asp','management','management.php','management.aspx','management.asp','signin','signin.php','signin.aspx','signin.asp','log-in','log-in.php','sign_in','sign_in.php','accounts','accounts.php','accounts.aspx','accounts.asp','auth.php','cp.php','cp.aspx','cp.asp','cp','moderator.php','moderator.aspx','moderator.asp','moderator','controlpanel','controlpanel.php','controlpanel.aspx','controlpanel.aspx','controlpanel.asp','wp-login.php','wp-admin','admins','admins.php','admins.aspx','admins.asp','administrators','panel','cpanel','wp-login','UserLogin','cmsadmin','admin_login.php','admin_login.aspx','admin_login.asp','admincp','admincp.php','admincp.aspx','admincp.asp','adminarea','admincontrol','admincontrol.php','admincontrol.aspx','admincontrol.aspx','administrators.php','administrators.aspx','administrators.asp','adminsite','adminpanel.php','adminpanel.asp','adminpanel.aspx','adminpanel','siteadmin','siteadmin.php','siteadmin.aspx','siteadmin.asp','secure','webmaster','webmaster.php','webmaster.aspx','webmaster.asp','root','secret','secrets']
    for i in lists:
        Nurl = url+"/"+i
        try:
            openurl = request.urlopen(Nurl)
            print(colored("[+]Found","green"))
            print(colored(Nurl,"green"))
            break
        except:
            print(colored("[-]Not Found","red"))
            print(colored(Nurl,"red"))   
            
elif x =="4":
    print(colored("// Example: https://www.google.com","yellow"))
    url =  input("Enter Site >>> ")
    lists = ['Navir.php','wso.php','Wso.php','c99','wso2018.php','alfa.php','1337w0rm.php','r57.php','1.php','2.php','3.php','4.php','Alfa.php','CGI.pl','K2ll33d','adminer.php','cwo.pl','3turr.php','Indoxploit.php','shell.php','Hack.php']
    for i in lists:
        Nurl = url+"/"+i
        try:
            request.urlopen(Nurl)
            print(colored("[+]Found","green"))
            print(colored(Nurl,"green"))
            break
        except:
            print(colored("[-]Not Found","red"))
            print(colored(Nurl,"red"))  
    
else:
    print("Try Again")
