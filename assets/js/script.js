// Datos de los proyectos
const proyectosData = [
  {
    titulo: 'Informativo_Cyberguard',
    descripcion: 'Pagina informativa de cyberseguridad.',
    imagenes: [
      '/assets/img/cg1.jpg',
      '/assets/img/cg2.jpg',
      '/assets/img/cg3.jpg'
    ],
    repo: 'https://github.com/danielantonio-driod/m-dulo_2/tree/master/cyberguard'
  },
  {
    titulo: 'Proyecto 2',
    descripcion: 'Este proyecto está en desarrollo, vuelve pronto.',
    imagenes: [],
    repo: '#'
  },
  {
    titulo: 'Proyecto 3',
    descripcion: 'Este proyecto está en desarrollo, vuelve pronto.',
    imagenes: [],
    repo: '#'
  },
  {
    titulo: 'Proyecto 4',
    descripcion: 'Este proyecto está en desarrollo, vuelve pronto.',
    imagenes: [],
    repo: '#'
  },
  {
    titulo: 'Proyecto 5',
    descripcion: 'Este proyecto está en desarrollo, vuelve pronto.',
    imagenes: [],
    repo: '#'
  }
];

let intervalId;
let currentModalIndex = 0;

// Abrir modal dinámicamente desde JS y mostrar imágenes en carrusel
function abrirProyectoPorIndice(index) {
  currentModalIndex = index;
  const { titulo, descripcion, imagenes, repo } = proyectosData[index];
  const modal = document.getElementById('modal');
  const galeria = document.getElementById('modal-imagenes');
  const link = document.getElementById('modal-github');

  // Limpiar contenido anterior
  galeria.innerHTML = '';
  clearInterval(intervalId);

  // Asignar contenido
  document.getElementById('modal-titulo').innerText = titulo;
  document.getElementById('modal-descripcion').innerText = descripcion;
  link.href = repo;

  // Crear galería de imágenes rotativas
  if (imagenes.length > 0) {
    let indexImg = 0;
    const img = document.createElement('img');
    img.src = imagenes[indexImg];
    img.alt = titulo;
    img.style.width = '100%';
    galeria.appendChild(img);

    // Rotar imágenes automáticamente
    intervalId = setInterval(() => {
      indexImg = (indexImg + 1) % imagenes.length;
      img.src = imagenes[indexImg];
    }, 2500);
  }

  modal.classList.remove('oculto');

  // Agregar controles de navegación solo una vez
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

// Navegación entre proyectos en el modal
function navegarModal(direccion) {
  currentModalIndex = (currentModalIndex + direccion + proyectosData.length) % proyectosData.length;
  abrirProyectoPorIndice(currentModalIndex);
}

// Cerrar el modal
function cerrarModal() {
  clearInterval(intervalId);
  document.getElementById('modal').classList.add('oculto');
}

// Controlar envío del formulario de contacto
const form = document.getElementById('formulario');
if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('confirmacion').classList.remove('oculto');
    this.reset();
  });
}

// Carrusel en sección proyectos
let currentSlide = 0;
function moverCarrusel(direccion) {
  const slides = document.querySelectorAll('.proyecto');
  if (!slides.length) return;
  slides[currentSlide].classList.add('oculto');
  currentSlide = (currentSlide + direccion + slides.length) % slides.length;
  slides[currentSlide].classList.remove('oculto');

  const modalVisible = !document.getElementById('modal').classList.contains('oculto');
  if (modalVisible) {
    abrirProyectoPorIndice(currentSlide);
  }
}

// Mostrar solo el primer proyecto al cargar
document.addEventListener('DOMContentLoaded', () => {
  const proyectos = document.querySelectorAll('.proyecto');
  proyectos.forEach(p => p.classList.add('oculto'));
  if (proyectos[0]) proyectos[0].classList.remove('oculto');

  // Clic en tarjetas de proyecto
  proyectos.forEach((proyecto, index) => {
    proyecto.addEventListener('click', () => {
      abrirProyectoPorIndice(index);
    });
  });
});

// Cierre del modal al hacer clic fuera del contenido
document.addEventListener('click', (e) => {
  const modal = document.getElementById('modal');
  const contenido = document.querySelector('.modal-contenido');
  const clickedNav = e.target.closest('.modal-btn');
  const clickedProyecto = e.target.closest('.proyecto');

  if (!modal.classList.contains('oculto') && !contenido.contains(e.target) && !clickedNav && !clickedProyecto) {
    cerrarModal();
  }
});

// Cierre con tecla Escape y navegación con flechas
document.addEventListener('keydown', (e) => {
  const modalVisible = !document.getElementById('modal').classList.contains('oculto');
  if (!modalVisible) return;

  if (e.key === 'Escape') cerrarModal();
  if (e.key === 'ArrowRight') navegarModal(1);
  if (e.key === 'ArrowLeft') navegarModal(-1);
});

// Botón flotante para ir arriba
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Mostrar u ocultar botón según scroll
window.addEventListener('scroll', () => {
  const boton = document.getElementById('btn-ir-arriba');
  if (window.scrollY > 300) {
    boton.style.display = 'block';
  } else {
    boton.style.display = 'none';
  }
});
