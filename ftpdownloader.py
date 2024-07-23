from ftplib import FTP
import os
import zipfile

def download_ftp_directory(ftp, remote_dir, local_dir):
    os.makedirs(local_dir, exist_ok=True)
    ftp.cwd(remote_dir)
    file_list = ftp.nlst()

    for file_name in file_list:
        local_file_path = os.path.join(local_dir, file_name)
        with open(local_file_path, 'wb') as local_file:
            ftp.retrbinary('RETR ' + file_name, local_file.write)

def zip_directory(local_dir, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                           os.path.join(local_dir, '..')))
    print(f"Files zipped successfully to {zip_filename}")

if __name__ == "__main__":
    # FTP server details
    ftp_server = 'https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_01'
    ftp_user = ''
    ftp_password = ''
    remote_dir = '/path/to/remote/ftp/folder'
    local_dir = 'ftp_download'

    # Connect and download files
    ftp = FTP(ftp_server)
    ftp.login(user=ftp_user, passwd=ftp_password)

    download_ftp_directory(ftp, remote_dir, local_dir)

    ftp.quit()

    # Zip the downloaded files
    zip_filename = 'ftp_download.zip'
    zip_directory(local_dir, zip_filename)
