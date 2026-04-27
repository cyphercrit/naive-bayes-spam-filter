from download_data import DownloadData

def main() -> None:
    try:
        # Download and extract data
        data_downloader = DownloadData(
            [
                "20021010_easy_ham.tar.bz2",
                "20021010_hard_ham.tar.bz2",
                "20021010_spam.tar.bz2",
                "20030228_easy_ham.tar.bz2",
                "20030228_easy_ham_2.tar.bz2",
                "20030228_hard_ham.tar.bz2",
                "20030228_spam.tar.bz2",
                "20030228_spam_2.tar.bz2",

            ],
            "https://spamassassin.apache.org/old/publiccorpus/"
        )
        data_downloader.download_data()

        
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()