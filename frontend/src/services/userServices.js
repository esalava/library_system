import { createRequest } from "@/utils/requestUtils";

export const getLibrosPrestados = async (username) => {
    const res = await createRequest().get(`/library/user/${username}`);
    return res;
};

export const solicitarUnLibro = async (username, data) => {
    const res = await createRequest().post(`library/user/${username}/prestar`, data);
    return res;
}

export const devolverLibro = async(username, prestamoId) => {
    const res = await createRequest().post(`library/user/${username}/devolver`, null,
    {params:{
        prestamo_id: prestamoId
    }})
    return res;
} 