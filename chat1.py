import json
import socket
from bs4 import BeautifulSoup
import requests
def server_program():
    host = socket.gethostname()
    port = 6666
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(15)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(4096).decode()
        print(f"from {address[0]}: "+ str(data))
        if data[:9] == 'net-info:':
            import requests
            import urllib.parse
            abc = data[9:]
            o = requests.get(abc)
            g = urllib.parse.urlparse(abc)
            ip = socket.gethostbyname(g.netloc)
            s1 = 'https://ipinfo.io/' + ip
            t = requests.get(s1)
            p = json.loads(t.text)
            data1, data2, data3, data4, data5, data6, data7 = p['city'], p['region'], p['country'], p['loc'], p['org'], p['postal'], p['timezone']
            inf=[f"ip-address: {ip},"f"cookies: {o.cookies}",f"port-regarding website: {g.port}",f'city-where-ip-belongs:{data1}',f'region-where-ip-belongs {data2}',f"country: {data3}",f"coordinates: {data4}",f'orgnaization :{data5}',f"postal-code: {data6}",f"timezone: {data7}"]
            dump=json.dumps(inf)
            conn.send(dump.encode())
        elif data=='movie-mumbai':
            import requests
            from bs4 import BeautifulSoup
            abc = []
            wec = []
            url = 'https://in.bookmyshow.com/explore/movies-mumbai'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=='movie-banglore':
            wec = []
            abc = []
            url = 'https://in.bookmyshow.com/explore/movies-bengaluru'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=='movie-hyderabad':
            wec = []
            abc = []
            url = 'https://in.bookmyshow.com/explore/movies-hyderabad'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=='movie-kolkata':
            wec = []
            abc = []
            url = 'https://in.bookmyshow.com/explore/movies-kolkata'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=='movie-kochi':
            abc = []
            wec = []
            url = 'https://in.bookmyshow.com/explore/movies-kochi'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=='movie-delhi':
            abc = []
            wec = []
            url = 'https://in.bookmyshow.com/explore/movies-national-capital-region-ncr'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=='movie-chennai':
            wec = []
            abc = []
            url = 'https://in.bookmyshow.com/explore/movies-chennai'
            req = requests.get(url)
            text = req.text
            soap = BeautifulSoup(text, 'html.parser')
            for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
                p = links.get_text()
                # print(p)
                wec.append(p)
            for i in wec:
                q = ['Tamil, Telugu', 'Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi',
                     'English, Hindi',
                     'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi',
                     'Kannada, Telugu, Hindi',
                     'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam',
                     'Browse by Cinemas',
                     'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu, Kannada',
                     'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
                if i not in q:
                    abc.append(i)
        elif data=="CHAT":
            info="hello user lets chat its open to all----:D"
            conn.send(info.encode())
            while True:
                message = input(" -> ")
                conn.send(message.encode())
                recv = conn.recv(102400).decode()
                print(recv)
                def language(lan):
                    return f"You are using {lan} for communication I can understand that language man :D"
                from langdetect import detect
                lang=detect(recv)
                if lang !='en':
                    language(lan=lang)
                from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
                analyse = SentimentIntensityAnalyzer()
                output = analyse.polarity_scores(recv)
                for i in output:
                    if i['score'] < 0.6:
                        print(f'please mind your language user {address}')
                    elif i['score'] < 0.5:
                        print(f'please control your language user {address}')
                    elif i['score'] <0.4:
                        print(f'I am disconnecting you')
                        conn.close()
        else:
            conn.send("hai buddy".encode())
if __name__ == '__main__':
    server_program()