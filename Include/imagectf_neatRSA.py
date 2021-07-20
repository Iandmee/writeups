import math
n1 = 129851722357947445345870990963660632711447373178135819868899984182659557798630904818907679897656671090445195493024305192175998357725180728308641342052877827178063748226956003293995628809809946890377677500727765422671309139577956460806060356061643066260620532143971581138444887013251083401740953016800526561369
n1_trash_with_q = 354020441161271454238824233113483251424739165273603253089281992413904299790750998993004221545361940017125675049620866260946107295019570616958455252820784279420662013197185267268535478305987123286908618637917837561207744990593948143827775524857529903243255631176220324605682439947302448209103973570727852816857845902079
ct = 99860436465836391865653329628063911057946675204553849493647896562280037248239340521968032740474787220879813274343214941793443913638426853461368251451691055571860562982592326807064465612371566427699272833229440737810391158841432366489390151103656479013891591734401496841642436054950303923680083243969093719406
e = 65537
q = math.gcd(n1, n1_trash_with_q)
p = n1//q
phi = (q-1)*(p-1)
d = pow(e, -1, phi)
print(bytes.fromhex(str(hex(pow(ct, d, n1)))[2:]).decode())