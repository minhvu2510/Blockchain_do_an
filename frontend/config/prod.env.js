module.exports = {
  BASE_URL: '"/pbx"',
  // BASE_URL: '""',
	NODE_ENV: '"production"',
	ENV_CONFIG: '"prod"',
	BASE_API: '"https://api-stagging-callcenter.vccloud.vn/v1"',
  APP_URL: `'${process.env.DEPLOY_PATH ? process.env.DEPLOY_PATH : '"http://test-develop.voice.test.vce.vn"'}'`,
  SSO_URL: '"https://manage.vccloud.vn/cas"',
  SOCKET_SERVER: '"https://api-stagging-callcenter.vccloud.vn/supervisor"'
}
