import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  async fetchRandomResource () {
    const res = await $axios.get(`random`)
    return res.data
  },

  async clearRandomCache () {
    const res = await $axios.get(`clear`)
    return res.data
  },

  async getJson (name) {
    const res = await $axios.get(`json/` + name)
    return res.data
  },

  async postJson (name, data) {
    console.log(data)
    const res = await $axios.post(`json/` + name, data)
    return res.data
  }
}
