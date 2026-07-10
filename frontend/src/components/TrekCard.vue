<template>

    <div class="col-md-4 mb-4">
        <div class="card shadow h-100">
            <img :src="trek.image_url" class="card-img-top" style="height:220px;object-fit:cover">
            <div class="card-body">
                <h5>
                    {{ trek.trek_name }}
                </h5>
                <p>
                    {{ trek.location }}
                </p>
                <p>
                    {{ trek.difficulty }}
                </p>
                <p>
                    ₹ {{ trek.price }}
                </p>
                <router-link :to="'/treks/' + trek.id" class="btn btn-success w-100">
                    View Details
                </router-link>
            </div>
        </div>
    </div>

</template>

<script setup>

defineProps({
    trek: Object
})

</script>