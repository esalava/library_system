import { createRequest } from "@/utils/requestUtils";

export const getPrestamosActuales = async () => {
    const res = await createRequest().get(`/library/admin/`);
    return res;
};

export const agregarNuevoLibro = async (nuevoLibro) => {
    const res = await createRequest().post('library/admin/registrar/', nuevoLibro);
    return res;
};