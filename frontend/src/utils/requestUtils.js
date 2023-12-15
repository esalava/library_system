import axios_core from "axios"
import {toastMessage} from "./sweetAlerts"

const API_URL = 'http://127.0.0.1:8000'

export const axiosConfig = {
    SERVER_NAME: API_URL,
    HEADERS: {
        "Content-Type": "application/json",
    }
};


export const createRequest = (timeout) => {
    const instance =  axios_core.create({
        baseURL: axiosConfig.SERVER_NAME,
        headers: axiosConfig.HEADERS,
        timeout,
    });
    instance.interceptors.response.use(
        (response) => {
            return response.data;
        },
        (error) => {
            if (error.response?.status == 400){
                const errmsg  = error.response.data;
                toastMessage("error", errmsg);
            } else {
                //mostrar un toast message
            }
            return Promise.reject(error)
        }
    );

    return instance;

}

export const axios = axios_core.create({
    baseURL: axiosConfig.SERVER_NAME,
    headers: axiosConfig.HEADERS,
});