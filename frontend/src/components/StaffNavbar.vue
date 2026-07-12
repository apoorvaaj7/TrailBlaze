<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-success sticky-top shadow">
        <div class="container">
            <router-link to="/staff/dashboard" class="navbar-brand fw-bold"><i class="fa-regular fa-snowflake"></i>
                TrailBlaze
            </router-link>
            <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#staffNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            &nbsp; &nbsp;
            <router-link class="nav-link" to="/staff/dashboard">
                Dashboard
            </router-link>
            <div class="collapse navbar-collapse" id="staffNavbar">
                <ul class="navbar-nav ms-auto align-items-center">
                    <li class="nav-item">
                        <button class="btn btn-outline-light ms-3" @click="logout"><i class="fa-solid fa-right-from-bracket me-2"></i>
                            Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

</template>

<script setup>

    import { useRouter } from "vue-router"

    const router = useRouter()
    const logout = () => {
        localStorage.clear()
        router.push("/login")
    }

</script>