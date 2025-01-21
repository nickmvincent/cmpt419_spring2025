import { defineSetupVue3 } from '@slidev/types'

export default defineSetupVue3(({ app, router }) => {
  const scaleContent = () => {
    const slides = document.querySelectorAll('.slidev-layout > :first-child')
    
    slides.forEach(slide => {
      const container = slide.parentElement
      const containerWidth = container.clientWidth
      const containerHeight = container.clientHeight
      const contentWidth = slide.scrollWidth
      const contentHeight = slide.scrollHeight
      
      // Calculate scale for both dimensions
      const scaleX = containerWidth / contentWidth
      const scaleY = containerHeight / contentHeight
      
      // Use the smaller scale to maintain aspect ratio, but allow up to 150% scaling
      const scale = Math.min(
        Math.min(scaleX, scaleY),
        1.5  // Allow scaling up to 150%
      )
      
      // Apply scaling transform and center the content
      slide.style.transform = `scale(${scale})`
    })
  }
  
  // Add event listeners
  if (typeof window !== 'undefined') {
    window.addEventListener('resize', scaleContent)
    router.afterEach(() => {
      // Wait a bit longer for layout to settle
      setTimeout(scaleContent, 200)
    })
  }
})