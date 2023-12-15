<template>
    <div>
      <h1>Administrador</h1>
    </div>
    <v-container>
      <v-dialog width="500">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" text="Agregar Libro"> </v-btn>
        </template>
        <template v-slot:default="{ isActive }">
          <v-card title="Agregar Libro">
            <v-form>
              <v-container>
                <v-row>
                  <v-col
                  cols="12"
                  >
                    <v-text-field
                    v-model="titulo"
                    label="Titulo"
                    ></v-text-field>

                    <v-text-field
                    v-model="autor"
                    label="Autor"
                    ></v-text-field>
                    
                    <v-text-field
                    v-model="codigo"
                    label="Código"
                    ></v-text-field>
                    
                    <v-text-field
                    v-model="cantidad"
                    label="Cantidad"
                    ></v-text-field>

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
                text="Agregar"
                @click="agregarLibro"
              ></v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
    </v-container>
    <h2>Libros Prestados de Todos los Usuarios</h2>
    <div v-for="prestamo in prestamosActuales" :key="prestamo.id">
        <Loan :isUser=false :prestamo="prestamo" />
    </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import {getPrestamosActuales, agregarNuevoLibro} from '@/services/adminServices';
  import Loan from '@/components/Loan.vue';

  const prestamosActuales  = ref(null);
  const overlay = ref(false);
  const titulo = ref('');
  const autor = ref('');
  const codigo = ref('');
  const cantidad = ref(1);

  const agregarLibro = async () => {
    await agregarNuevoLibro({
      'titulo': titulo.value,
      'autor': autor.value,
      'cantidad_disponible': cantidad.value,
      'codigo': codigo.value,
    });
    limpiarCampos();
    await actualizarPrestamosActuales();
  }

  const limpiarCampos = () => {
    titulo.value = '';
    autor.value = '';
    codigo.value = '';
    cantidad.value = 1;
  }

  const actualizarPrestamosActuales = async () => {
    const resLibrosPrestados = await getPrestamosActuales();
    prestamosActuales.value = resLibrosPrestados.data;
  }

  onMounted(async () => {
    await actualizarPrestamosActuales();
  });
  </script>