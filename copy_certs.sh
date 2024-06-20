docker cp mysql-ssl:/var/lib/mysql/ca.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/ca-key.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/client-cert.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/client-key.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/private_key.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/public_key.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/server-cert.pem metabase-mysql-certs/.
docker cp mysql-ssl:/var/lib/mysql/server-key.pem metabase-mysql-certs/.
cat metabase-mysql-certs/ca.pem metabase-mysql-certs/client-key.pem > metabase-mysql-certs/client.pem