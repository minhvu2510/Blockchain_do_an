import request from '@/utils/request'

export function loginByUsername(email, password) {
    const data = {
        email,
        password
    }
    return request({
        url: '/login',
        method: 'post',
        data
    })
}

export function logout() {
    return request({
        url: '/auth/logout',
        method: 'delete'
    })
}

export function getUserInfo(token) {
    return request({
        url: '/user',
        method: 'get',
        params: { token }
    })
}

