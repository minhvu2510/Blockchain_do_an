const getters = {
  token: state => state.user.token,
  email: state => state.user.email,
  account: state => state.user.account,
  role: state => state.user.role,
  id: state => state.user.id,
  check: state => state.user.check
}
export default getters
