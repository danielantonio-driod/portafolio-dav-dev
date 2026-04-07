// ========================
// DATOS DE PROYECTOS
// ========================
const proyectosData = [
    {
    titulo: 'ERP del Taller D-Labs Suite',
    descripcion: 'Sistema interno para gestionar clientes, cotizaciones, ventas, inventario y finanzas en un flujo integrado.',
    imagenes: [
      'static/img/proyectos/erp-login.png',
      'static/img/proyectos/erp-dashboard.png',
      'static/img/proyectos/erp-clientes.png',
      'static/img/proyectos/erp-cotizaciones.png',
      'static/img/proyectos/erp-inventario.png'
    ],
    repo: 'https://soydlabs.com'
    },
    {
    titulo: 'Pagina Web del Taller (soydlabs.com)',
    descripcion: 'Sitio publico del taller orientado a conversion, branding y acceso al portal de clientes.',
        imagenes: [
      'static/img/proyectos/web-home.png',
      'static/img/proyectos/web-login-portal.png',
      'static/img/proyectos/web-portal.png'
        ],
    repo: 'https://soydlabs.com'
    },
    {
    titulo: 'IA Local - Agente Juan',
    descripcion: 'Asistente de IA local para gestionar recursos del homelab y consultas operativas en lenguaje natural.',
    imagenes: [
      'static/img/proyectos/ia-juan.png'
    ],
        repo: '#'
    }
];

let intervalId;             // Para controlar el cambio de imagen automático
let currentModalIndex = 0;  // Índice del proyecto actual en el modal

// ========================
// ABRIR MODAL
// ========================
let currentImgIndex = 0;  // Índice actual de imagen en el modal

function abrirProyectoPorIndice(index) {
  currentModalIndex = index;
  currentImgIndex = 0;  // Reiniciar al primera imagen
  const { titulo, descripcion, imagenes, repo } = proyectosData[index];
  const modal = document.getElementById('modal');
  const galeria = document.getElementById('modal-imagenes');
  const link = document.getElementById('modal-github');

  galeria.innerHTML = '';       // Limpiar imágenes anteriores
  clearInterval(intervalId);    // Detener cualquier carrusel anterior

  document.getElementById('modal-titulo').innerText = titulo;
  document.getElementById('modal-descripcion').innerText = descripcion;
  link.href = repo;

  if (repo === '#') {
    link.style.display = 'none';
  } else {
    link.style.display = 'inline-block';
  }

  // Galería de imágenes rotativas si existen
  if (imagenes.length > 0) {
    let indexImg = 0;
    const imgContainer = document.createElement('div');
    imgContainer.style.position = 'relative';
    imgContainer.style.width = '100%';
    
    const img = document.createElement('img');
    img.src = imagenes[indexImg];
    img.alt = titulo;
    img.style.width = '100%';
    imgContainer.appendChild(img);
    
    // Añadir contador de imágenes si hay más de una
    if (imagenes.length > 1) {
      const contador = document.createElement('div');
      contador.id = 'modal-contador';
      contador.style.textAlign = 'center';
      contador.style.marginTop = '8px';
      contador.style.fontSize = '10px';
      contador.style.color = '#666';
      contador.style.fontFamily = 'Press Start 2P';
      contador.innerText = `${indexImg + 1} de ${imagenes.length}`;
      imgContainer.appendChild(contador);
    }
    
    galeria.appendChild(imgContainer);

    intervalId = setInterval(() => {
      indexImg = (indexImg + 1) % imagenes.length;
      img.src = imagenes[indexImg];
      currentImgIndex = indexImg;
      
      // Actualizar contador
      const cnt = document.getElementById('modal-contador');
      if (cnt) cnt.innerText = `${indexImg + 1} de ${imagenes.length}`;
    }, 2500);
  }

  modal.classList.remove('oculto');

  // Agregar controles de navegación si no existen aún
  if (!document.getElementById('modal-controles')) {
    const controles = document.createElement('div');
    controles.id = 'modal-controles';
    controles.classList.add('modal-nav');
    controles.innerHTML = `
      <button class="modal-btn" onclick="navegarImagenModal(-1)">&#9664; Anterior</button>
      <button class="modal-btn" onclick="navegarImagenModal(1)">Siguiente &#9654;</button>
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
// NAVEGACIÓN ENTRE IMÁGENES DENTRO DEL MODAL
// ========================
function navegarImagenModal(direccion) {
  const { imagenes } = proyectosData[currentModalIndex];
  if (imagenes.length === 0) return;
  
  clearInterval(intervalId);  // Pausar el carrusel automático
  
  currentImgIndex = (currentImgIndex + direccion + imagenes.length) % imagenes.length;
  const img = document.querySelector('#modal-imagenes img');
  const cnt = document.getElementById('modal-contador');
  
  if (img) {
    img.src = imagenes[currentImgIndex];
    if (cnt) cnt.innerText = `${currentImgIndex + 1} de ${imagenes.length}`;
  }
  
  // Reanudar carrusel automático
  let autoIndex = currentImgIndex;
  intervalId = setInterval(() => {
    autoIndex = (autoIndex + 1) % imagenes.length;
    if (img) img.src = imagenes[autoIndex];
    if (cnt) cnt.innerText = `${autoIndex + 1} de ${imagenes.length}`;
    currentImgIndex = autoIndex;
  }, 2500);

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
