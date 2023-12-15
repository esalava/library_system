<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/library/user/esalavarria/" class="nav-link" active-class="active">Usuario</RouterLink>
        <RouterLink to="/library/admin/" class="nav-link" active-class="active">Admin</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
.swal-toast {
  z-index: 9999;
}

.swal-toast-container {
  z-index: 9999;
}

.nav-link {
  margin-top: 10px;
  text-decoration: none;
  color: #333; 
  padding: 5px 10px; 
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-link.active {
  background-color: #f0f0f0; 
  color: #000;
}
</style>
