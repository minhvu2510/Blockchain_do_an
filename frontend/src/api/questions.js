import request from '@/utils/request'

export function get_question() {
    return request({
        url: '/get_quetstions',
        method: 'get'

    })
}
export function notify() {
    return request({
        url: '/notify',
        method: 'get'

    })
}
export function answers(data) {
    return request({
        url: '/receive_answers',
        method: 'post',
        data
    })
}

export function getinfo(data) {
    return request({
        url: '/give_info',
        method: 'post',
        data
    })
}
