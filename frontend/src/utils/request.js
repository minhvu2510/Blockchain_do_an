import axios from 'axios'
import { Notification } from 'element-ui'
import store from '@/store'
import { getToken ,getTokenOtp } from '@/utils/auth'

// create an axios instance
const service = axios.create({
  baseURL: process.env.BASE_API, // api base_url
  timeout: 10000 // request timeout
})

// request interceptor
service.interceptors.request.use(config => {
  // Do something before request is sent
  // config.headers['Content-Type'] = 'application/json'
  if (store.getters.token) {
    config.headers['Authorization'] = getToken()
    config.headers['Tokenotp'] = getTokenOtp()
    // config.headers['Token_otp'] =  getToken()
    config.headers['Content-Type'] = 'application/json'
  }
  return config
}, error => {
  // Do something with request error
  console.log(error) // for debug
  Promise.reject(error)
})

// respone interceptor
service.interceptors.response.use(
  response => response,
  /**
   * The following note through the response custom code to indicate the status of the request,
   * when the code returns the following conditions for permission problems, log out and return to the login page
   * Such as xmlhttprequest state code identification logic can be written in the following error
   */
    //  const res = response.data;
    //     if (res.code !== 20000) {
    //       Message({
    //         message: res.message,
    //         type: 'error',
    //         duration: 5 * 1000
    //       });
    //       // 50008: illegal token; 50012: other client login; 50014: Token expired;
    //       if (res.code === 50008 || res.code === 50012 || res.code === 50014) {
    //         MessageBox.confirm('You have been logged out, you can cancel the stay on the page, or re-login, OK to log out', {
    //           confirmButtonText: 'OK',
    //           cancelButtonText: 'Cancel',
    //           type: 'warning'
    //         }).then(() => {
    //           store.dispatch('FedLogOut').then(() => {
    //             location.reload();// In order to re-instantiate the vue-router object to avoid bugs
    //           });
    //         })
    //       }
    //       return Promise.reject('error');
    //     } else {
    //       return response.data;
    //     }
  error => {
    console.log('err', error)// for debug
    Notification.error({
      title: 'Lỗi(requet)',
      message:error,
      duration: 4000
    })
    console.log(error)
    console.log('-----',error.response.data)
    // store.dispatch('LogOut')
    if (error.response.data.description === 'Permission denied.') {
      setTimeout(() => {
        console.log('Missing Authorization Header')
        store.dispatch('LogOut')
      }, 1000)
    }
    if (error.response.data.msg === 'Token has expired') {
      setTimeout(() => {
        store.dispatch('LogOut')
      }, 1000)
    }
    if (error.response.data.message.Authorization === 'Missing required parameter in the HTTP headers') {
      setTimeout(() => {
        store.dispatch('LogOut')
      }, 1000)
    }
    if (error.response.data.msg === 'Token has been revoked') {
      setTimeout(() => {
        console.log('Missing Authorization Header')
        store.dispatch('LogOut')
      }, 1000)
    }
    return Promise.reject(error)
  })

export default service
