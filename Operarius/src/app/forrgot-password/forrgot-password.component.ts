import { Component, OnInit } from '@angular/core';
import { AuthService } from '../shared/services/auth.service';
@Component({
selector: 'app-forrgot-password',
templateUrl: './forrgot-password.component.html'
})
export class ForgotPasswordComponent implements OnInit {
constructor(
public authService: AuthService
) { }
ngOnInit() {
}
}
