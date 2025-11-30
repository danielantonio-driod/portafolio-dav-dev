// ========================
// DATOS DE PROYECTOS
// ========================
const proyectosData = [
    {
        titulo: 'Portfolio Personal',
        descripcion: 'Este sitio web, construido con HTML, CSS y JavaScript puro.',
        imagenes: [],
        repo: 'https://github.com/danielantonio-driod/portafolio-dav-dev'
    },
    {
        titulo: 'Informativo_Cyberguard',
        descripcion: 'Página informativa de ciberseguridad desarrollada con tecnologías web estándar.',
        imagenes: [
            'static/img/cg1.jpg',
            'static/img/cg2.jpg',
            'static/img/cg3.jpg'
        ],
        repo: 'https://github.com/danielantonio-driod/m-dulo_2/tree/master/cyberguard'
    },
    {
        titulo: 'Próximos Proyectos',
        descripcion: 'Más proyectos en camino...',
        imagenes: [],
        repo: '#'
    }
];

let intervalId;             // Para controlar el cambio de imagen automático
let currentModalIndex = 0;  // Índice del proyecto actual en el modal

// ========================
// ABRIR MODAL
// ========================
function abrirProyectoPorIndice(index) {
  currentModalIndex = index;
  const { titulo, descripcion, imagenes, repo } = proyectosData[index];
  const modal = document.getElementById('modal');
  const galeria = document.getElementById('modal-imagenes');
  const link = document.getElementById('modal-github');

  galeria.innerHTML = '';       // Limpiar imágenes anteriores
  clearInterval(intervalId);    // Detener cualquier carrusel anterior

  document.getElementById('modal-titulo').innerText = titulo;
  document.getElementById('modal-descripcion').innerText = descripcion;
  link.href = repo;

  // Galería de imágenes rotativas si existen
  if (imagenes.length > 0) {
    let indexImg = 0;
    const img = document.createElement('img');
    img.src = imagenes[indexImg];
    img.alt = titulo;
    img.style.width = '100%';
    galeria.appendChild(img);

    intervalId = setInterval(() => {
      indexImg = (indexImg + 1) % imagenes.length;
      img.src = imagenes[indexImg];
    }, 2500);
  }

  modal.classList.remove('oculto');

  // Agregar controles de navegación si no existen aún
  if (!document.getElementById('modal-controles')) {
    const controles = document.createElement('div');
    controles.id = 'modal-controles';
    controles.classList.add('modal-nav');
    controles.innerHTML = `
      <button class="modal-btn" onclick="navegarModal(-1)">&#9664;</button>
      <button class="modal-btn" onclick="navegarModal(1)">&#9654;</button>
    `;
    document.querySelector('.modal-contenido').appendChild(controles);
  }

  // Sincronizar fondo del carrusel
  const slides = document.querySelectorAll('.proyecto');
  slides.forEach(s => s.classList.add('oculto'));
  if (slides[index]) slides[index].classList.remove('oculto');
  currentSlide = index;
}

// ========================
// NAVEGACIÓN ENTRE PROYECTOS
// ========================
function navegarModal(direccion) {
  currentModalIndex = (currentModalIndex + direccion + proyectosData.length) % proyectosData.length;
  abrirProyectoPorIndice(currentModalIndex);
}

// ========================
// CERRAR MODAL
// ========================
function cerrarModal() {
  clearInterval(intervalId);
  document.getElementById('modal').classList.add('oculto');
}

// ========================
// CARRUSEL DE PROYECTOS
// ========================
let currentSlide = 0;

function moverCarrusel(direccion) {
  const slides = document.querySelectorAll('.proyecto');
  if (!slides.length) return;

  slides[currentSlide].classList.add('oculto');
  currentSlide = (currentSlide + direccion + slides.length) % slides.length;
  slides[currentSlide].classList.remove('oculto');

  // Si el modal está visible, actualiza su contenido
  const modalVisible = !document.getElementById('modal').classList.contains('oculto');
  if (modalVisible) {
    abrirProyectoPorIndice(currentSlide);
  }
}

// ========================
// AL CARGAR LA PÁGINA
// ========================
document.addEventListener('DOMContentLoaded', () => {
  const proyectos = document.querySelectorAll('.proyecto');
  proyectos.forEach(p => p.classList.add('oculto'));
  if (proyectos[0]) proyectos[0].classList.remove('oculto');

  proyectos.forEach((proyecto, index) => {
    // Solo agregar el evento a los proyectos que no sean la sección de descargas
    const isDescarga = proyecto.querySelector('a.btn-django.btn-success[download]');
    if (!isDescarga) {
      proyecto.addEventListener('click', () => {
        abrirProyectoPorIndice(index);
      });
    }
  });
});

// ========================
// CERRAR MODAL AL HACER CLIC FUERA
// ========================
document.addEventListener('click', (e) => {
  const modal = document.getElementById('modal');
  const contenido = document.querySelector('.modal-contenido');
  const clickedNav = e.target.closest('.modal-btn');
  const clickedProyecto = e.target.closest('.proyecto');

  if (!modal.classList.contains('oculto') && !contenido.contains(e.target) && !clickedNav && !clickedProyecto) {
    cerrarModal();
  }
});

// ========================
// TECLAS: ESC y FLECHAS
// ========================
document.addEventListener('keydown', (e) => {
  const modalVisible = !document.getElementById('modal').classList.contains('oculto');
  if (!modalVisible) return;

  if (e.key === 'Escape') cerrarModal();
  if (e.key === 'ArrowRight') navegarModal(1);
  if (e.key === 'ArrowLeft') navegarModal(-1);
});

// ========================
// BOTÓN FLOTANTE - IR ARRIBA
// ========================
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Mostrar u ocultar el botón al hacer scroll
window.addEventListener('scroll', () => {
  const boton = document.getElementById('btn-ir-arriba');
  if (boton) {
    boton.style.display = window.scrollY > 300 ? 'block' : 'none';
  }
});
