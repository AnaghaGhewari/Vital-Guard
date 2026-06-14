import axios from 'axios'

export const AUTH_TOKEN_STORAGE_KEY = 'vitalguard.authToken'

const client = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? '',
  headers: {
    'Content-Type': 'application/json',
  },
})

client.interceptors.request.use((config) => {
  const token =
    typeof window !== 'undefined'
      ? window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
      : null

  config.headers = config.headers ?? {}

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})

export default client
