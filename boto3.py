

def main():
    # Upload
    print(data_access_s3.upload_to_s3())

    # Download
    data_access_s3.download_from_s3()


if __name__ == '__main__':   # dunder
    main()
