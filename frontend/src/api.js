//intersepter using axios
//check if we have an access token and if we do add it

import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
}

)