<template>
  <div class="container vh-100 d-flex justify-content-center align-items-center">
    <div class="card shadow p-4" style="width:500px">
      <h2 class="text-center mb-4">
        TrailBlaze
      </h2>
      <h5 class="text-center mb-4">
        Register
      </h5>
      <form>
        <div class="mb-3">
          <label>Name</label>
          <input class="form-control" v-model="name">
        </div>
        <div class="mb-3">
          <label>Email</label>
          <input type="email" class="form-control" v-model="email">
        </div>
        <div class="mb-3">
          <label>Phone</label>
          <input class="form-control" v-model="phone">
        </div>
        <div class="mb-3">
          <label>Address</label>
          <textarea class="form-control" v-model="address"></textarea>
        </div>
        <div class="mb-4">
          <label>Password</label>
          <input type="password" class="form-control" v-model="password">
        </div>
        <button class="btn btn-success w-100">
          Register
        </button>
      </form>
      <hr>
      <p class="text-center">
        Already have an account?
        <router-link to="/login">
          Login
        </router-link>
      </p>
    </div>
  </div>
</template>

<script setup>

import { ref } from "vue"

const name = ref("")
const email = ref("")
const phone = ref("")
const address = ref("")
const password = ref("")

</script>