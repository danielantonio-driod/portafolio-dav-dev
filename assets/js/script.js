const proyectosData = [
  {
    titulo: 'Control de Órdenes',
    descripcion: 'Sistema para registrar y gestionar órdenes en un taller.',
    imagenes: [
      'https://via.placeholder.com/600x400/ffcc00/000000?text=Proyecto+1-1',
      'https://via.placeholder.com/600x400/0000ff/ffffff?text=Proyecto+1-2',
      'https://via.placeholder.com/600x400/ffcc00/000000?text=Proyecto+1-3'
    ],
    repo: 'https://github.com/usuario/control-ordenes'
  },
  {
    titulo: 'Agenda Médica',
    descripcion: 'App para gestionar citas médicas fácilmente.',
    imagenes: [
      'https://via.placeholder.com/600x400/ff0000/ffffff?text=Proyecto+2-1',
      'https://via.placeholder.com/600x400/ffffff/000000?text=Proyecto+2-2',
      'https://via.placeholder.com/600x400/0000ff/ffffff?text=Proyecto+2-3'
    ],
    repo: 'https://github.com/usuario/agenda-medica'
  },
  {
    titulo: 'Sistema de Inventario',
    descripcion: 'Herramienta para controlar inventario con alertas inteligentes.',
    imagenes: [
      'https://via.placeholder.com/600x400/000000/ffffff?text=Proyecto+3-1',
      'https://via.placeholder.com/600x400/ffcc00/000000?text=Proyecto+3-2',
      'https://via.placeholder.com/600x400/0000ff/ffffff?text=Proyecto+3-3'
    ],
    repo: 'https://github.com/usuario/inventario'
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

function abrirModal(titulo, descripcion, imagenes = [], repo = '#') {
  const modal = document.getElementById('modal');
  const galeria = document.getElementById('modal-imagenes');
  const link = document.getElementById('modal-github');

  document.getElementById('modal-titulo').innerText = titulo;
  document.getElementById('modal-descripcion').innerText = descripcion;
  link.href = repo;

  galeria.innerHTML = '';

  if (imagenes.length > 0) {
    let index = 0;
    const img = document.createElement('img');
    img.src = imagenes[index];
    img.alt = titulo;
    img.style.width = '100%';
    galeria.appendChild(img);

    intervalId = setInterval(() => {
      index = (index + 1) % imagenes.length;
      img.src = imagenes[index];
    }, 2500);
  }

  modal.classList.remove('oculto');

  // Agregar botones de navegación al modal (después del contenido)
  const navControlesExistente = document.getElementById('modal-controles');
  if (!navControlesExistente) {
    const controles = document.createElement('div');
    controles.id = 'modal-controles';
    controles.classList.add('modal-nav');
    controles.innerHTML = `
      <button class="modal-btn" onclick="navegarModal(-1)">&#9664;</button>
      <button class="modal-btn" onclick="navegarModal(1)">&#9654;</button>
    `;
    document.querySelector('.modal-contenido').appendChild(controles);
  }
}

function abrirProyectoPorIndice(index) {
  currentModalIndex = index;
  const proyecto = proyectosData[index];
  abrirModal(proyecto.titulo, proyecto.descripcion, proyecto.imagenes, proyecto.repo);

  // Sincronizar el fondo del carrusel
  const slides = document.querySelectorAll('.proyecto');
  slides.forEach(s => s.classList.add('oculto'));
  if (slides[index]) slides[index].classList.remove('oculto');
  currentSlide = index;
}

function cerrarModal() {
  clearInterval(intervalId);
  document.getElementById('modal').classList.add('oculto');
}

const form = document.getElementById('formulario');
if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('confirmacion').classList.remove('oculto');
    this.reset();
  });
}

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

document.addEventListener('DOMContentLoaded', () => {
  const proyectos = document.querySelectorAll('.proyecto');
  proyectos.forEach(p => p.classList.add('oculto'));
  if (proyectos[0]) proyectos[0].classList.remove('oculto');
});

// Cerrar modal con Escape o clic fuera del contenido

// Modificación aquí: ignorar click en botones de navegación

document.addEventListener('click', (e) => {
  const modal = document.getElementById('modal');
  const contenido = document.querySelector('.modal-contenido');
  const clickedProyecto = e.target.closest('.proyecto');
  const clickedNav = e.target.closest('.modal-btn');

  if (!modal.classList.contains('oculto') && !contenido.contains(e.target) && !clickedProyecto && !clickedNav) {
    cerrarModal();
  }
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') cerrarModal();
});

document.addEventListener('keydown', (e) => {
  const modalVisible = !document.getElementById('modal').classList.contains('oculto');
  if (!modalVisible) return;

  if (e.key === 'ArrowRight') navegarModal(1);
  if (e.key === 'ArrowLeft') navegarModal(-1);
});

function navegarModal(direccion) {
  currentModalIndex = (currentModalIndex + direccion + proyectosData.length) % proyectosData.length;
  abrirProyectoPorIndice(currentModalIndex);
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.addEventListener('scroll', () => {
  const boton = document.getElementById('btn-ir-arriba');
  if (window.scrollY > 300) {
    boton.style.display = 'block';
  } else {
    boton.style.display = 'none';
  }
});
