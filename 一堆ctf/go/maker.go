/*
 * @Author: s1rius
 * @Date: 2023-09-17 18:45:44
 * @LastEditTime: 2023-09-17 18:58:25
 * @Description: https://s1rius.space/
 */
package main

import (
	"image"
	"image/color"
	"image/draw"
	"image/png"
	"log"
	"os"

	"github.com/goki/freetype"
	// "golang.org/x/image/bmp"
	"golang.org/x/image/math/fixed"
)

func test() {
	img := image.NewRGBA(image.Rect(0, 0, 2000, 1000))

	bgColor := color.White
	draw.Draw(img, img.Bounds(), &image.Uniform{C: bgColor}, image.Point{}, draw.Src)

	text := "H"
	fontFile, err := os.ReadFile("C:\\home\\ctf\\docker\\go\\JetBrainsMono-Regular.ttf")
	if err != nil {
		log.Fatal(err)
	}
	// fontBytes, err := io.ReadAll(fontFile)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	font, err := freetype.ParseFont(fontFile)
	if err != nil {
		log.Fatal(err)
	}

	c := freetype.NewContext()
	c.SetDst(img)
	c.SetSrc(image.NewUniform(color.Black))
	c.SetFontSize(12)
	c.SetFont(font)

	pt := fixed.P(0, 0)
	_, err = c.DrawString(text, pt)
	if err != nil {
		return
	}

	file, err := os.Create("hello.png")
	if err != nil {
		log.Fatal(err)
	}

	err = png.Encode(file, img)
	if err != nil {
		log.Fatal(err)
	}
	err = file.Close()
	if err != nil {
		return
	}
}
