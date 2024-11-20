import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-contador',
  imports: [],
  templateUrl: './contador.component.html',
  styleUrl: './contador.component.css'
})
export class ContadorComponent implements OnInit {

    constructor() { }

    ngOnInit(): void {

    }

   number:number = 1;

   incrementar() {
    this.number++
   }

   decrementar() {
    this.number--
   }

}
