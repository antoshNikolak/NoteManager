//intersepter using axios
//check if we have an access token and if we do add it
//adds teh correct headers so we dont have to manually add them.

import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

// we have specified the base url so when using this api we just need to say the path
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config

    },
    (error) => {
        return Promise.reject(error)
    }
)

export default api