<style>
.book-info {
  color: red;
}
</style>
<template>
    <div class="d-flex">
      <v-card class="mb-4 ml-4" color="purple-lighten-4" width="400">
        <v-card-title>{{ book.titulo }}</v-card-title>
        <v-card-subtitle>{{ book.autor}}</v-card-subtitle>
        <v-card-text>Código:{{ book.codigo}}<br/>Cantidad: {{book.cantidad_disponible}}</v-card-text>
        <v-dialog width="500">
          <template v-slot:activator="{ props }">
          <v-btn v-bind="props" text="Prestar este libro"  v-if="isUser" color="indigo-darken-3"> </v-btn>
          </template>
          <template v-slot:default="{ isActive }">
            <v-card>
            <v-card-title>Solicitud de libro: {{ book.titulo }}</v-card-title>
            <v-form>
              <v-container>
                <v-row>
                  <v-col
                  cols="12"
                  >
                  <v-date-picker v-model="fechaDevolucion"></v-date-picker>
                </v-col>
                </v-row>
              </v-container>

            </v-form>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                text="Cerrar"
                @click="isActive.value = false"
              ></v-btn>
              <v-btn
                text="Solicitar Libro"
                @click="solicitarLibro(book.id)"
              ></v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
      </v-card>
    </div>
    
</template>
<script setup>
import { defineProps, ref, defineEmits } from 'vue';
import { useRoute } from 'vue-router';
import {format} from 'date-fns';
import {solicitarUnLibro} from '@/services/userServices';
import {toastMessage} from '@/utils/sweetAlerts';

const username = ref('');
const route = useRoute();
const fechaDevolucion = ref(null);

const  emit  = defineEmits(['libro-solicitado']);
const props = defineProps({
  book: {
    type: Object,
    required: true
  },
  isUser: {
    type: Boolean,
    required: true
  }
});

const solicitarLibro = async (id) => {
  username.value = route.params.username;
  if(!fechaDevolucion.value){
    toastMessage("error", "No tiene fecha seleccionada")
  }
  const formattedDate = format(fechaDevolucion.value, 'yyyy-MM-dd');
  const data = {
    "libro_id": id,
    "fecha_fin": formattedDate
  }
  const res = await solicitarUnLibro(username.value, data);
  emit('libro-solicitado', username.value);
};
</script>
