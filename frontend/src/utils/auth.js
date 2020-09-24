import Cookies from 'js-cookie'

const TokenKey = 'Admin-Token'
const TokenKeyOtp = 'Admin-Token-Otp'
const user = 'User'
const CookieKey = 'session'

export function getToken() {
  return Cookies.get(TokenKey)
}
export function getTokenOtp() {
  return Cookies.get(TokenKeyOtp)
}
export function getUser() {
  return Cookies.get(user)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}
export function setTokenOtp(token) {
  return Cookies.set(TokenKeyOtp, token)
}
export function setUser(token) {
  return Cookies.set(user, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function getCookie() {
  return Cookies.get(CookieKey)
}
