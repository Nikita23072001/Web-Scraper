import { AuthService } from './../shared/services/auth.service';
import { Component, OnInit } from '@angular/core';
@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  ngOnInit(): void {}


  // tslint:disable-next-line:member-ordering
  constructor(
    public authService: AuthService) {}
}

