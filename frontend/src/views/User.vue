<template>
    <div>
      <h1>Bienvenido, {{ username }}</h1>
      <h2>Catálogo Disponible</h2>
      <div class="d-flex flex-wrap">
        <div v-for="book in catalogo" :key="book.id">
          <Book :book="book" :isUser=true @libro-solicitado="handleLibroSolicitado"/>
        </div>
      </div>
      <h2>Libros Prestados</h2>
      <div class="d-flex flex-wrap">
        <div v-for="prestamo in librosPrestados" :key="prestamo.id">
          <Loan :prestamo="prestamo" :isUser=true @libro-devuelto="handleLibroDevuelto"/>
        </div>
      </div>

    </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import {getLibrosPrestados} from '@/services/userServices';
  import {getCatalogoDisponible} from '@/services/libraryServices';
  import Book from '@/components/Book.vue';
  import Loan from '@/components/Loan.vue';
  
  const username = ref('');
  const catalogo = ref(null);
  const librosPrestados = ref(null);
  
  const route = useRoute();
  
  const handleLibroSolicitado = async (id) => {
    await actualizarUserPage();
  };

  const handleLibroDevuelto = async(id) => {
    await actualizarUserPage();
  }

  const actualizarUserPage = async()=>{
    username.value = route.params.username;
    const resLibrosPrestados = await getLibrosPrestados(username.value);
    const resCatalogoDisponible = await getCatalogoDisponible();

    catalogo.value = resCatalogoDisponible.data;
    librosPrestados.value = resLibrosPrestados.data;
  }

  onMounted(async () => {
    await actualizarUserPage();
  });
  </script>
  