import { Router } from '@angular/router';
import { AuthService } from './../shared/services/auth.service';
import { Component, OnInit, NgZone } from '@angular/core';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  constructor(public data: AuthService,
              public router: Router,
              public ngZone: NgZone) {
   }

  ngOnInit() {
  }

}
