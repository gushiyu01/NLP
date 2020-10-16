from authlib.jose import jwt


header = {'alg': 'HS256'}
payload = {'iss': 'Authlib', 'sub': '123', 'name': 'bob'}
secret = '123abc.'
token = jwt.encode(header, payload, secret)
print(token.decode())

claims = jwt.decode(token, secret)
print(claims)
print(claims.header)
print(claims.validate_aud())
