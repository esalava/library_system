import { createRequest } from "@/utils/requestUtils";

export const getCatalogoDisponible = async () => {
    const res = await createRequest().get(`/library/catalogo`);
    return res;
};

