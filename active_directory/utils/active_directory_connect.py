# load modules 
import os
from ldap3 import Server, Connection, ALL



def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing or empty environment variable: {name}")
    return value




def active_directory_connect():
    try:
        ad_username =   require_env('ACTIVE_DIRECTORY_USERNAME')
        ad_password =   require_env('ACTIVE_DIRECTORY_PASSWORD')
        ad_server   =   require_env('ACTIVE_DIRECTORY_SERVER')

        # Connect to the server
        bind_dn = ad_username
    
        
        server = Server(ad_server, use_ssl=True, get_info=ALL)
        conn = Connection(server, bind_dn, ad_password)

        # Check if the connection is successful
        if not conn.bind():
            return None, "Failed to connect to Active Directory"

        return conn, "Successfully connected to Active Directory", 
    except Exception as e:
        return None, f"Error connecting to Active Directory: {str(e)}"


def run():
    ad_connection_object, message = active_directory_connect()
    if message:
        print(message)



if __name__ == "__main__":
    run()

