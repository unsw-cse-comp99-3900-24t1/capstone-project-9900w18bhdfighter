const shortName = (firstName = '', lastName = '') => {
  console.log('firstName:', firstName)

  return firstName.charAt(0).toUpperCase() + lastName.charAt(0).toUpperCase()
}

const isDarkColor = (color = '') => {
  const rgb = parseInt(color.substring(1), 16)
  const r = (rgb >> 16) & 0xff
  const g = (rgb >> 8) & 0xff
  const b = (rgb >> 0) & 0xff
  const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
  return luminance < 140
}
const stringToColorPair = (input = '') => {
  const colors = [
    '#1abc9c', // 绿松石
    '#2ecc71', // 翡翠
    '#3498db', // 深蓝
    '#9b59b6', // 紫罗兰
    '#34495e', // 湿石板
    '#16a085', // 绿海
    '#27ae60', // 草地
    '#2980b9', // 奈利
    '#8e44ad', // 鬼王
    '#2c3e50', // 海军蓝
    '#f1c40f', // 太阳花
    '#e67e22', // 胡萝卜
    '#e74c3c', // 苍红
    '#ecf0f1', // 云
    '#95a5a6', // 混凝土
  ]

  let hash = 0
  for (let i = 0; i < input.length; i++) {
    hash = input.charCodeAt(i) + ((hash << 5) - hash)
  }
  hash = Math.abs(hash)

  const color1 = colors[hash % colors.length]

  const color2 = isDarkColor(color1) ? '#FFFFFF' : '#000000'

  return [color1, color2]
}

// 使用示例

export { shortName, isDarkColor, stringToColorPair }
