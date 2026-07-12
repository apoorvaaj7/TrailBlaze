<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-success fixed-top shadow">
        <div class="container">
            <router-link
                to="/dashboard" class="navbar-brand fw-bold">
                <i class="fa-solid fa-mountain me-2"></i>
                TrailBlaze
            </router-link>
            <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            &nbsp; &nbsp;
            <router-link class="nav-link" to="/dashboard">
                Dashboard
            </router-link>
            <div class="collapse navbar-collapse" id="navbar">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <router-link to="/my-treks" class="nav-link">
                            My Treks
                        </router-link>
                    </li>
                    <li class="nav-item ms-3">
                        <button class="btn btn-outline-light" @click="logout">
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

    const logout = () =>{
        localStorage.clear()
        router.push("/login")
    }
</script>