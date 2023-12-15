<template>
    <div class="book-info">
      <v-card class="mb-4 ml-4" width="400" color="grey-lighten-2">
        <v-card-title>{{ prestamo.libro__titulo }}</v-card-title>
        <v-card-subtitle>Autor: {{ prestamo.libro__autor }}</v-card-subtitle>
        <v-card-text>
          Préstamo Id: {{prestamo.id}}<br/>
          Código:{{ prestamo.libro__codigo }}<br/>
          Fecha prestamo: {{ prestamo.fecha_inicio}}<br/>
          Fecha fin:{{ prestamo.fecha_fin}}</v-card-text>
        <v-card-text>Pedido por:{{ prestamo.usuario__username}}</v-card-text>
        <v-btn text="Devolver Libro" v-if="isUser" @click="devolucionLibro(prestamo.id)"  color="indigo-darken-3"/>
        <br/>
      </v-card>
    </div>
</template>
<script setup>
import { ref, defineProps, defineEmits} from 'vue';
import {devolverLibro} from '@/services/userServices';
import { useRoute } from 'vue-router';

const route = useRoute();
const username = ref('');
const  emit  = defineEmits(['libro-devuelto']);

const devolucionLibro = async (id) => {
  username.value = route.params.username;
  const res = await devolverLibro(username, id);
  emit('libro-devuelto', username.value)
}

const props = defineProps({
  prestamo: {
    type: Object,
    required: true
  },
  isUser: {
    type: Boolean,
    required: true
  }
});
</script>