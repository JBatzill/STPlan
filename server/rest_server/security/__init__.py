from OpenSSL import crypto


# creates a key and certificate pair and saves it in the given files
# if they dont exist, it creates the files.

def create_key_certificate_pair(host, country, company, years, key_file, cert_file):
    # create a key pair
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 1024)

    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = country
    cert.get_subject().O = company
    cert.get_subject().CN = host
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(years*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha1')

    c = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
    k = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)


    open(cert_file, "wb").write(c)
    open(key_file, "wb").write(k)
