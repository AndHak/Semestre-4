import { Component, OnInit } from '@angular/core';
import { blob } from 'stream/consumers';

@Component({
  selector: 'app-botones',
  imports: [],
  templateUrl: './botones.component.html',
  styleUrl: './botones.component.css'
})
export class BotonesComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
      
  }

  text_color:string = '';

  button_disabled:boolean = false;

}
